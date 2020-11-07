with import <nixpkgs> {};

mkShell {
  buildInputs = [ (python27.withPackages (ps: with ps; [ pygame pillow pycairo numpy pygobject3 termcolor setproctitle ])) ];
}
