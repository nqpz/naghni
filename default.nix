with import <nixpkgs> {};
stdenv.mkDerivation {
    name = "naghni";
    buildInputs = [ (python27.withPackages (ps: with ps; [ pygame pillow pycairo numpy pygobject3 termcolor setproctitle ])) ];
}
