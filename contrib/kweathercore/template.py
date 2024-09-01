pkgname = "kweathercore"
pkgver = "24.08.0"
pkgrel = 0
build_style = "cmake"
# needs to get location
make_check_args = ["-E", "locationquerytest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "kholidays-devel",
    "qt6-qtbase-devel",
    "qt6-qtpositioning-devel",
]
pkgdesc = "KDE Weather library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kweathercore/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kweathercore-{pkgver}.tar.xz"
)
sha256 = "ada469144f2cd75f70c6d474b965e3d5cf49c80c4f3270fad36399889126b1b2"


@subpackage("kweathercore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()