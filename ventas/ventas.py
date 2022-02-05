from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

inventario=[
	{'codigo': '111', 'nombre': 'leche 1L', 'precio': 20.0, 'cantidad': 20},
	{'codigo': '222', 'nombre': 'cereal 500g', 'precio': 50.5, 'cantidad': 15}, 
	{'codigo': '333', 'nombre': 'yogurt 1L', 'precio': 25.0, 'cantidad': 10},
	{'codigo': '444', 'nombre': 'helado 2L', 'precio': 80.0, 'cantidad': 20},
	{'codigo': '555', 'nombre': 'alimento para perro 20kg', 'precio': 750.0, 'cantidad': 5},
	{'codigo': '666', 'nombre': 'shampoo', 'precio': 100.0, 'cantidad': 25},
	{'codigo': '777', 'nombre': 'papel higiénico 4 rollos', 'precio': 35.5, 'cantidad': 30},
	{'codigo': '888', 'nombre': 'jabón para trastes', 'precio': 65.0, 'cantidad': 5},
	{'codigo': '999', 'nombre': 'refresco 600ml', 'precio': 15.0, 'cantidad': 10}
]

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
  ''' Adds selection and focus behaviour to the view. '''
  touch_deselect_last = BooleanProperty(True)


class SelectableBoxLayout(RecycleDataViewBehavior, BoxLayout):
  ''' Add selection support to the Label '''
  index = None
  selected = BooleanProperty(False)
  selectable = BooleanProperty(True)

  def refresh_view_attrs(self, rv, index, data):
    self.index = index
    self.ids['_hashtag'].text = str(1+index)
    self.ids['_articulo'].text = data['nombre'].capitalize()
    self.ids['_cantidad'].text = str(data['cantidad_carrito'])
    self.ids['_precio_por_articulo'].text = str("{:.2f}".format(data['precio']))
    self.ids['_precio'].text = str("{:.2f}".format(data['precio_total']))
    return super(SelectableBoxLayout, self).refresh_view_attrs(
        rv, index, data)

  def on_touch_down(self, touch):
    ''' Add selection on touch down '''
    if super(SelectableBoxLayout, self).on_touch_down(touch):
      return True
    if self.collide_point(*touch.pos) and self.selectable:
      return self.parent.select_with_touch(self.index, touch)

  def apply_selection(self, rv, index, is_selected):
    ''' Respond to the selection of items in the view. '''
    self.selected = is_selected
    if is_selected:
      print("selection changed to {0}".format(rv.data[index]))
    else:
      print("selection removed for {0}".format(rv.data[index]))

class RV(RecycleView):
  def __init__(self, **kwargs):
    super(RV, self).__init__(**kwargs)
    self.data = []

class VentasWindow(BoxLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def agregar_producto_codigo(self, codigo):
    for producto in inventario:
      if codigo == producto['codigo']:
        articulo = {}
        articulo['codigo'] = producto['codigo']
        articulo['nombre'] = producto['nombre']
        articulo['precio'] = producto['precio']
        articulo['cantidad_carrito'] = 1
        articulo['cantidad_inventario'] = producto['cantidad']
        articulo['precio_total'] = producto['precio']
        self.ids.rvs.data.append(articulo)
        break

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