pkgname=batterylet
pkgver=1.0
pkgrel=1
pkgdesc="Get notified when battery runs low."
arch=('any')
url="https://github.com/coderkwan/batterylet"
install=batterylet.install
license=('MIT')
depends=('python' 'python-pillow' 'tk')
source=("https://github.com/coderkwan/batterylet")
md5sums=('SKIP')

package() {
     install -d "$pkgdir/opt/batterylet"
     install -Dm755 "$srcdir/"* "$pkgdir/opt/batterylet"
    install -Dm644 "$srcdir/batterylet.service" "$pkgdir/usr/lib/systemd/user/batterylet.service"
}
