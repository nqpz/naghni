with import <nixpkgs> {};
stdenv.mkDerivation {
    name = "naghni";
    buildInputs = [ (python27.withPackages (ps: with ps; [ pygame pillow pycairo numpy pygobject3 termcolor setproctitle ]))
                    gnome2.python_rsvg
                  ];

    shellHook = ''
      export PYTHONPATH=${gnome2.python_rsvg}/lib/python2.7/site-packages/gtk-2.0:$PYTHONPATH
    '';
}
