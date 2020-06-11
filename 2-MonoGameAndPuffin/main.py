# Imported DLLs here are available to all scripts
import clr

import platform, os, sys
from distutils.dir_util import copy_tree

class Main:    
    def run(self):
        self._import_monogame_dlls()
        self._copy_monogame_transitive_dependencies()
        self._import_puffin_dlls()

        print("Starting ...")
        # Have to import after MononoGame imports
        from dummy_game import DummyGame
        DummyGame(1024, 540).Run()
        print("Bye!!")

    def _import_monogame_dlls(self):
        print("Importing MonoGame DLLs ...")
        for dll in os.listdir("lib"):
            print("Importing {}".format(dll))
            clr.AddReferenceToFileAndPath("lib\\{}".format(dll))
    
    def _copy_monogame_transitive_dependencies(self):
        print("Copying transitive MonoGame dependencies ...")
        # MonoGame depends on libSDL + OpenAL DLLs. Import the right (platform/architecture) ones
        # for our current OS and architecture.
        operating_system = platform.system() # Windows, Linux, or Darwin
        runtime = "linux"

        if operating_system == "Darwin":
            runtime = "osx"
        elif operating_system == "Linux":
            runtime = "linux"
        elif operating_system == "Windows":
            runtime = "win"

        architecture = 'x64'
        if sys.maxsize <= 2**32:
            architecture = 'x86'

        source_dir = os.path.join('runtimes', "{}-{}".format(runtime, architecture))
        destination_dir = os.path.join("Puffin", "Puffin.Infrastructure.MonoGame", "bin", "Debug", "netstandard2.0")
        copy_tree(source_dir, destination_dir)
        print("Copied from {} to {}".format(source_dir, destination_dir))
    
    def _import_puffin_dlls(self):
        print("Importing Puffin DLLs ...")  
        clr.AddReferenceToFileAndPath("Puffin\\Puffin.Core\\bin\\Debug\\netstandard2.0\\Puffin.Core.dll")
        clr.AddReferenceToFileAndPath("Puffin\\Puffin.Infrastructure.MonoGame\\Bin\\Debug\\netstandard2.0\\Puffin.Infrastructure.MonoGame.dll")
        # TODO: import UI/controls DLL here

Main().run()