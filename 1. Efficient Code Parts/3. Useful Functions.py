 ### ****************
 ### USEFUL FUNCTIONS
 ### ****************

##################################################
### The Timer
##################################################

import time
from contextlib import contextmanager
@contextmanager
def timer():
    t0 = time.time()
    yield
    t1 = time.time()
    print( 'Runtime: ' + str(round(t1-t0,2)) + ' sn' )



##################################################
### The Null Detector
##################################################


def null_detector(x):
    missing = x.isnull().sum()
    missing = missing[missing > 0]
    missing.sort_values(ascending=False, inplace=True)
    
    fig, ax = plt.subplots(figsize=(15,6) )
    sns.barplot( x=missing.index, y=missing.values)
    plt.title( f'Total Column: {x.shape[1]} --- Missing Column: {len(missing)} ({round(len(missing)*100/x.shape[1],2)}%) ' )
    plt.xticks(rotation=60)
    
    for p in ax.patches:
        ax.annotate( '{:.2f}'.format(p.get_height()/x.shape[0]),  (p.get_x() + 0.1, p.get_height() + 3), fontsize=11 )  
    plt.show()


##################################################
### The xxx
##################################################









