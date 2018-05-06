import numpy as np
import matplotlib as mpl

def plotError(errorArray, landmarks):
    '''
    Visualizes deviation from mean in all three directions + Euclidean distance

    INPUT:
        errorArray - Contains the deviation in each direction [4xN]
        landmarks - Labels for each fiducial [1xN]

    OUTPUT:
        fig - Generated visualization figure with deviations
    '''

    fig = mpl.pyplot.figure(figsize=(20, 20))

    # Generate plots for each array
    for i in range(4):

        # Switch cases
        if i == 0:
            title = 'Deviation in X'
        elif i == 1:
            title = 'Deviation in Y'
        elif i == 2:
            title = 'Deviation in Z'
        elif i == 3:
            title = 'Euclidean Distance'

        ax = fig.add_subplot(2, 2, i+1)

        hist = ax.bar(range(len(errorArray[:, i])), errorArray[:, i])

        # Plot properties
        ax.set_title('%s \nmax = %.3f mm, min = %.3f mm' % (title, max(np.absolute(errorArray[:, i])),
                                                      min(np.absolute(errorArray[:, i]))),
                                                      fontsize=16, fontweight='bold')
        ax.set_ylabel('Deviation from mean [mm]', fontsize=14, fontweight='bold')
        ax.set_xlabel('Landmarks', fontsize=14, fontweight='bold')
        ax.set_xticks(range(0, len(errorArray[:, i]), 1))
        ax.set_xticklabels(landmarks, rotation=90)
        ax.set_xlim([-.5, len(errorArray[:, i])-.5])
        ax.tick_params(axis='both', which='major', labelsize=12, length=7, pad=5, width=1,
                                direction='inout', top='off', right='off')
        ax.spines['top'].set_linewidth(2)
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['left'].set_linewidth(2)
        ax.spines['right'].set_linewidth(2)
        ax.yaxis.grid(color='k', alpha=0.2)

    fig.tight_layout()

    return fig
