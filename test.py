import unittest
import folium
import branca
from map_script import m  # Import your map object from the script

class TestMapCreation(unittest.TestCase):

    def test_map_exists(self):
        """Test if the map is created"""
        self.assertIsInstance(m, folium.Map)

    def test_map_location(self):
        """Test if map is centered at correct coordinates"""
        expected_location = (1.3021, 103.8641)  # The Projector
        self.assertEqual(m.location, expected_location)

    def test_map_tiles(self):
        """Ensure the Esri Satellite tile is added"""
        tiles = [layer.tile_name for layer in m._children.values() if isinstance(layer, folium.raster_layers.TileLayer)]
        self.assertIn("Esri.WorldImagery", tiles)

class TestMarkers(unittest.TestCase):

    def test_projector_marker_exists(self):
        """Check if The Projector marker is present"""
        markers = [child for child in m._children.values() if isinstance(child, folium.map.Marker)]
        projector_marker = next((marker for marker in markers if marker.location == [1.3021, 103.8641]), None)
        self.assertIsNotNone(projector_marker)

    def test_projector_popup(self):
        """Ensure The Projector has the correct iframe popup"""
        markers = [child for child in m._children.values() if isinstance(child, folium.map.Marker)]
        projector_marker = next((marker for marker in markers if marker.location == [1.3021, 103.8641]), None)
        self.assertIsNotNone(projector_marker)

        # Extract and check the popup content
        popup = projector_marker.options.get("popup")
        self.assertIsInstance(popup, folium.Popup)
        self.assertIn("https://theprojector.sg/", popup.get_name())

class TestFeatureGroup(unittest.TestCase):

    def test_feature_group_exists(self):
        """Ensure FeatureGroup is added to the map"""
        feature_groups = [layer for layer in m._children.values() if isinstance(layer, folium.map.FeatureGroup)]
        self.assertTrue(feature_groups, "FeatureGroup missing from the map.")

    def test_layer_control(self):
        """Check if the LayerControl is added"""
        layer_controls = [layer for layer in m._children.values() if isinstance(layer, folium.map.LayerControl)]
        self.assertTrue(layer_controls, "LayerControl is missing.")

if __name__ == "__main__":
    unittest.main()
