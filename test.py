
from pyramid.helper_functions import symmetries_filter
from pyramid.preprocessing import preprocessing
from pyramid.examples.small_pyramid import small_pyramid, small_pyramid_bricks


order1_sets = preprocessing(small_pyramid, small_pyramid_bricks)

order1_sets = symmetries_filter(small_pyramid, order1_sets)

print(order1_sets[0])
