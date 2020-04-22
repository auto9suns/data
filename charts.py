import matplotlib.pyplot as plt
import seaborn as sns


class charts():
    def __init__(self):
        pass
    def hist(self, data, mmm = False, **kwargs):
        """
        :param data: pandas Series
        :param mmm: if mark mode (only first mode), median, mean on the charts
        :param kwargs: args in seaborn.distplot
        :return:
        """
        sns.distplot(data, **kwargs)
        sns.set(rc={'axes.facecolor': '#EAEAF2', 'figure.facecolor': 'white'})
        """
        seaborn.set takes and rc argument that accepts a dictionary of valid matplotlib rcparams.
        So we need to set two things: the axes.facecolor, which is the color of the area where the 
        data are drawn, and the figure.facecolor, which is the everything a part of the figure 
        outside of the axes object
        """

        if mmm == True:
            mean, median, mode = data.mean(), data.median(), data.mode().get_values()[0]
            config = {'Mean': mean, 'Median': median, 'Mode': mode}
            color = {'Mean': "tomato", 'Median': "yellow", 'Mode': "limegreen"}
            for k in config:
                plt.axvline(config.get(k), color = color.get(k), linestyle="--", linewidth = "1")
            plt.legend(
                {'Mean {0}'.format(mean): mean, 'Median {0}'.format(median): median, 'Mode {0}'.format(mode): mode})
        plt.grid(True, color="white", linewidth="1")






