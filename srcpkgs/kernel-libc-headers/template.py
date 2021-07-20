pkgname = "kernel-libc-headers"
_mver = "5"
version = f"{_mver}.10.4"
revision = 0
wrksrc = f"linux-{version}"
make_cmd = "gmake"
short_desc = "Linux API headers for userland development"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
homepage = "http://www.kernel.org"

options = ["bootstrap"]

from cbuild import sites, cpu

distfiles = [f"{sites.kernel}/kernel/v{_mver}.x/linux-{version}.tar.xz"]
checksum = ["904e396c26e9992a16cd1cc989460171536bed7739bf36049f6eb020ee5d56ec"]

if not current.bootstrapping:
    hostmakedepends = ["gmake", "perl"]

_arch = cpu.match_target(
    "x86_64*", lambda a: "x86",
    "aarch64*", lambda a: "arm64",
    "ppc*", lambda a: "powerpc",
    "riscv64*", lambda a: "riscv",
)

def do_build(self):
    from cbuild.util import make
    import glob, shlex

    mk = make.Make(self, jobs = 1)

    tcfl = self.get_cflags(shell = True)
    tlfl = self.get_ldflags(shell = True)
    with self.profile(cpu.host()):
        hcfl = self.get_cflags(shell = True)
        hlfl = self.get_ldflags(shell = True)

    mk.invoke("mrproper", [
        "ARCH=" + _arch,
        "CC=clang -target " + self.build_profile.short_triplet,
        "HOSTCC=clang",
        "CFLAGS=" + tcfl,
        "HOSTCFLAGS=" + hcfl,
        "LDFLAGS=" + tlfl,
        "HOSTLDFLAGS=" + hlfl,
        "headers"
    ])

    # remove extra files and drm headers
    for fn in self.find(".*", files = True, root = self.abs_wrksrc):
        self.unlink(fn, root = self.abs_wrksrc)

    self.unlink("usr/include/Makefile", root = self.abs_wrksrc)
    self.rmtree("usr/include/drm", root = self.abs_wrksrc)

def do_install(self):
    self.install_files("usr/include", "usr")
