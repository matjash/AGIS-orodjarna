from qgis.core import QgsProcessingProvider
from PyQt5.QtGui import QIcon
import os
from pathlib import Path

#import algorithm
#from .fileslist import Files2Table
from .se_word_catalog import StratiWordCatalog
from .se_dmv import se_dmv
from .se_textures import se_textures
from .check_raster_sources import check_raster_sources
from ..externals import path

class Provider(QgsProcessingProvider):
    def __init__(self):
        self.plugin_dir = os.path.dirname(__file__)
        QgsProcessingProvider.__init__(self)
        
    def loadAlgorithms(self, *args, **kwargs):
        
        self.addAlgorithm(StratiWordCatalog())
        self.addAlgorithm(se_dmv())
        self.addAlgorithm(se_textures())
        self.addAlgorithm(check_raster_sources())
        

    def id(self):
        return 'agis_toolbox'
        
    def name(self, *args, **kwargs):
        """The human friendly name of your plugin in Processing.

        This string should be as short as possible (e.g. "Lastools", not
        "Lastools version 1.0.1 64-bit") and localised.
        """
        return self.tr('AGIS toolbox')

    def icon(self):
        """Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        icon = path('icons')/'agis_toolbox.png'
        return QIcon(str(icon))
        