from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class VentasWindow(BoxLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def agregar_producto_codigo(self, codigo):
    print("Se mando", codigo)

  def agregar_producto_nombre(self, nombre):
    print("Se mando", nombre)

  def eliminar_producto(self):
    print("Eliminar Producto Presionado")

  def modificar_producto(self):
    print("Modificar Producto Presionado")

  def pagar(self):
    print("Pagar")

  def nueva_compra(self):
    print("Nueva Compra")

  def admin(self):
    print("Admin Presionado")

  def signout(self):
    print("Sign Out Presionado")

class VentasApp(App):
  def build(self):
    return VentasWindow()


if __name__ == '__main__':
    VentasApp().run()