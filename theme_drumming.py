import matplotlib.pyplot as plt
from cycler import cycler
import matplotlib as mpl


def theme_drumming():
    # Font
    font = 'Helvetica'

    custom_palette = ["#7E1900", "#54B2CF"]

    # Create a dictionary of rcParams for the theme
    theme_settings = {

        # Font
        'font.family': font,

        # Titles
        'axes.titlesize': 20,
        'axes.titleweight': 'bold',
        'axes.titlepad': 10,

        # Axis titles
        'axes.labelsize': 16,
        'axes.labelweight': 'bold',

        # Axis text (ticks)
        'xtick.labelsize': 12,
        'ytick.labelsize': 12,
        # completely remove major x and y ticks
        #'xtick.major.size': 0,
        'ytick.major.size': 0,
        # remove minor ticks
        #'xtick.minor.size': 0,
        'ytick.minor.size': 0,

        # Grid and panel backgrounds
        'axes.grid': True,  # Enable grid globally
        'grid.color': '#cbcbcb',
        'grid.linestyle': '-',  # Solid grid lines
        'axes.edgecolor': 'white',
        'axes.facecolor': 'white',

        # Disable vertical grid lines (x-axis)
        'axes.grid.axis': 'y',  # Only horizontal (y-axis) grid lines
        'grid.alpha': 1.0,  # Gridline transparency
        'grid.linestyle': '-',  # Style for horizontal grid lines
        'grid.linewidth': 0.8,

        # Legend settings
        'legend.title_fontsize': 16,
        'legend.fontsize': 16,
        'legend.loc': 'upper right',
        'legend.frameon': True,  # Turn on the frame for the legend
        'legend.facecolor': 'white',  # Set white background for the legend
        # change legend opacity
        'legend.framealpha': 1,
        # change legend border color to white
        'legend.edgecolor': 'white',
        # make legend edges square
        'legend.fancybox': False,

        # Strip and facet settings
        'axes.spines.left': False,
        'axes.spines.bottom': False,
        'axes.spines.right': False,
        'axes.spines.top': False,

        # Additional settings
        'axes.titlelocation': 'left',

        # Set custom color palette for non-seaborn plots
        'axes.prop_cycle': cycler(color=custom_palette)
    }

    return theme_settings
