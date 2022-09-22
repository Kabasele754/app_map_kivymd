import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

KV = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import MapView,MapSource kivy_garden.mapview



<ExtendedButton>
    elevation: 3
    -height: "56dp"


<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    unfocus_color: "#fffcf4"


MDScreen:

    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDBoxLayout:
                    orientation: "vertical"

                   

                    MDBoxLayout:

                        MDNavigationRail:
                            id: navigation_rail
                            md_bg_color: "#fffcf4"
                            selected_color_background: "#e7e4c0"
                            ripple_color_item: "#e7e4c0"
                            on_item_release: app.switch_screen(*args)

                            #MDNavigationRailMenuButton:
                                #on_release: nav_drawer.set_state("open")

                            MDNavigationRailItem:
                                #md_bg_color: "#b0f0d6"
                                text: "Distance"
                                icon: "map-marker-distance"
                                

                            MDNavigationRailItem:
                                text: "Itinaire"
                                icon: "open-source-initiative"

                            MDNavigationRailItem:
                                text: "Position"
                                icon: "google-maps"

                            MDNavigationRailItem:
                                text: "Trafic"
                                icon: "bus-marker"

                            MDNavigationRailItem:
                                text: "Coffee"
                                icon: "coffee"
                            MDNavigationRailItem:
                                text: "Direction"
                                icon: "directions-fork"
                            MDNavigationRailItem:
                                text: "Human"
                                icon: "human-male-female"
                            MDNavigationRailItem:
                                text: "Proximité"
                                icon: "map-marker-radius"
                            

                        ScreenManager:
                            id: screen_manager
                            Screen:
                                name: "screen2"
                                BoxLayout:
                                    MapView:
                                        lat:-11.6843854
                                        lon:27.4758589
                                        zoom:14
                                        #on_zoom:
                                            #self.zoom = 3 if self.zoom < 12 else self.zoom
                                        #map_source:"osm"
                                        MapMarkerPopup:
                                            source:"images/marker.png"
                                            lat: -11.6843854
                                            lon: 27.4758589
                                            popup_size: 400,320
                                        MapMarkerPopup:
                                            source:"images/marker.png"
                                            lat: -11.6749507
                                            lon: 27.4671683
                                            popup_size: 400,320   
                                        
                                        MapMarkerPopup:
                                            source:"images/marker.png"
                                            lat: -11.6820316
                                            lon: 27.4814562
                                            popup_size: 400,320  
                           

    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 16, 16, 0)
        md_bg_color: "#fffcf4"
        elevation: 12
        width: "240dp"

        MDNavigationDrawerMenu:

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "12dp"
                padding: 0, 0, 0, "12dp"

                MDIconButton:
                    icon: "menu"

                ExtendedButton:
                    text: "Compose"
                    icon: "pencil"

            DrawerClickableItem:
                text: "Python"
                icon: "language-python"

            DrawerClickableItem:
                text: "JavaScript"
                icon: "language-javascript"

            DrawerClickableItem:
                text: "CPP"
                icon: "language-cpp"

            DrawerClickableItem:
                text: "Swift"
                icon: "language-swift"
'''


class ExtendedButton(
    RoundedRectangularElevationBehavior, MDFillRoundFlatIconButton
):
    '''
    Implements a button of type
    `Extended FAB <https://m3.material.io/components/extended-fab/overview>`_.

    .. rubric::
        Extended FABs help people take primary actions.
        They're wider than FABs to accommodate a text label and larger target
        area.

    This type of buttons is not yet implemented in the standard widget set
    of the KivyMD library, so we will implement it ourselves in this class.
    '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = "16dp"
        Clock.schedule_once(self.set_spacing)

    def set_spacing(self, interval):
        self.ids.box.spacing = "12dp"

    def set_radius(self, *args):
        if self.rounded_button:
            self._radius = self.radius = self.height / 4


class ContryMap(MDApp):
    def build(self):
        self.title = "Maps country"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def switch_screen(
        self, instance_navigation_rail, instance_navigation_rail_item
    ):
        '''
        Called when tapping on rail menu items. Switches application screens.
        '''

        #self.root.ids.screen_manager.current = (
            #instance_navigation_rail_item.icon.split("-")[1].lower()
        #)

    # def on_start(self):
    #     '''Creates application screens.'''

    #     navigation_rail_items = self.root.ids.navigation_rail.get_items()[:]
    #     navigation_rail_items.reverse()

    #     for widget in navigation_rail_items:
    #         name_screen = widget.icon.split("-")[1].lower()
    #         screen = MDScreen(
    #             name=name_screen,
    #             md_bg_color="#edd769",
    #             #radius=[10, 0, 0, 0],
    #         )
    #         box = MDBoxLayout(padding="12dp")
    #         label = MDLabel(
    #             text=name_screen.capitalize(),
    #             font_style="H1",
    #             halign="right",
    #             adaptive_height=True,
    #             shorten=True,
    #         )
    #         box.add_widget(label)
    #         screen.add_widget(box)
    #         self.root.ids.screen_manager.add_widget(screen)

if __name__=="__main__":
    ContryMap().run()