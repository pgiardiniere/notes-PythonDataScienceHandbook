# often, datasets of interest are missing key data
# or are otherwise not homogenous. Ch is dedicated to NaN, null, etc.

### Trade-offs in missing data conventions
# Many ways of nhandling missing data in table/DataFrame
# generally they fall into 2 categories:
    # Mask              which indicates missing vals globally
    # Sentinel Value    which indicates missing entry

# masking approach: mask may be an entirely seperate bool arr
# sentinel approach: sentinel val could be some data-specific convention
#                   (e.g.) missing int val  -9999 
#          or a more global convention (e.g. indicating missing float w/ NaN)