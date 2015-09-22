#!/usr/bin/python

"""
Telnet server
"""

from twisted.internet.protocol import ServerFactory
from twisted.conch.telnet import StatefulTelnetProtocol

import string

from Valmoor import Game
from player import Player
from humans import Human

import sys

from zope.interface import implements
from twisted.internet import protocol, reactor, task
from twisted.python import log

from twisted.cred import portal
from twisted.cred import checkers
from twisted.cred import credentials

from twisted.conch.telnet import AuthenticatingTelnetProtocol
from twisted.conch.telnet import StatefulTelnetProtocol
from twisted.conch.telnet import ITelnetProtocol
from twisted.conch.telnet import TelnetTransport
from twisted.conch.telnet import ECHO


class RegisteringTelnetProtocol(AuthenticatingTelnetProtocol):
    state = "Welcome"
    
    def connectionMade(self):
        self.transport.write("Welcome to the server!\n")
        self.transport.write("(L)ogin or (R)egister a new account?:   ")

    def telnet_Welcome(self, line):
        if line.strip().lower() == 'r':
            self.transport.write("\nEnter your new username: ")
            return "NewUserName"
        elif line.strip().lower() == 'l':
            self.transport.write('Username: ')
            return "User"
        self.transport.write("\nI don't understand that option.")
        return 'Welcome'
     
    def telnet_NewUserName(self, line):
        for checker in self.portal.checkers.values():
            print "Checking for user with name '%s' in %s" % (line, checker.users)
            if line in checker.users:
                self.transport.write("That account already exists!")
                return "Welcome"

        self.username = line
        self.transport.will(ECHO)
        self.transport.write("Enter your new password: ")
        return "NewPassword"
        
    def telnet_NewPassword(self, line):
        username, password = self.username, line
        self.addNewUser(self.username, line)
        return self.telnet_Password(line)
        
        # call the normal login method
        def login(ignored):
            creds = credentials.UsernamePassword(username, password)
            d = self.portal.login(creds, None, ITelnetProtocol)
            d.addCallback(self._cbLogin)
            d.addErrback(self._ebLogin)
        self.transport.wont(ECHO).addCallback(login)
        return 'Discard'
        
    def addNewUser(self, username, password):
        for checker in self.portal.checkers.values():
            checker.addUser(username, password)
        
    def _ebLogin(self, failure):
        self.transport.write("\nAuthentication failed: %s (%s)\n" % (failure, dir(failure)))
        self.state = "Welcome"
        self.connectionMade()

class Realm:
  implements(portal.IRealm)

  def requestAvatar(self, avatarId, mind, *interfaces):
    print "Requesting avatar..."
    #print avatarId
    #print mind
    if ITelnetProtocol in interfaces:
      av = MudProtocol()
      av.name = avatarId
      av.state = "Command"
      return ITelnetProtocol, av, lambda:None
    raise NotImplementedError("Not supported by this realm")


class MudProtocol(StatefulTelnetProtocol):

    def connectionMade(self):
        self.ip = self.transport.getPeer().host

        print "New connection from", self.ip

        self.msg_me("")
        self.msg_me("Welcome to the Kingdom of Valmoor")
 
        self.msg_me("")

        self.player = Human(game, game.reborn_loc)
        self.player.connection = self
        self.player.name = self.name
        
        print self.name + " has entered the Realm"
        
        self.player.wallet = 250             
        self.player.input_list.insert(0, "look")
        
 #       checker = portal_.checkers.values()[0]
 #       self.player.password = checker.users[self.player.name]
       
        if self.player.name in game.player_store:
            player_info = game.player_store[self.player.name]
            self.player.load_player(player_info)
        game.players.append(self.player)
        

      #
#        game.save()
  
            
    
    def connectionLost(self, reason):
        print "Lost connection to", self.ip
        try:
            game.players.remove(self.player)
        except:
            pass
        try:
            del self.player
        except:
            pass
            
    def lineReceived(self, line):
        line = line.replace('\r', '')
        line = ''.join([ch for ch in line if ch not in string.punctuation])
        self.player.input_list.insert(0, line)
        print "Received line: %s from %s (%s)" % (line, self.name, self.ip)
        return

    def msg_me(self, message):
      
        message = message.rstrip() + '\r'
        self.sendLine(message)
                

if __name__ == '__main__':

    print "Prototype MUD server running!"

    realm = Realm()
    portal_ = portal.Portal(realm)
    #print portal_.checkers

    checker = checkers.InMemoryUsernamePasswordDatabaseDontUse()
    checker.addUser("Vlad", "")
    checker.addUser("Drac", "")
    checker.addUser("Lor", "")
  
    
    portal_.registerChecker(checker)
    #print dir(checker)
    #print checker.users

    def run_one_tick():
        game.run_one_tick()

    game = Game()
    game_runner = task.LoopingCall(run_one_tick)
    game_runner.start(1.0)
    
    def do_save():
        print "Saving game...",
        game.save()
        print "game.players==>"
        print game.players
        print "player_store==>"
        print game.player_store
        print "done!"
 #       print "Updating portal passwords..."
 #       for player in game.player_store.values():
#            for checker in portal_.checkers.values():
#                checker.users[player['name']] = player['password']
    
 #   do_save()
    game_saver = task.LoopingCall(do_save)
    game_saver.start(20.0)
        
    factory = protocol.ServerFactory()
    factory.protocol = lambda: TelnetTransport(RegisteringTelnetProtocol, portal_)

    log.startLogging(sys.stdout)
    reactor.listenTCP(4242, factory)
    reactor.run()


