"""Mask on Demand items"""

class mask(object):
    """A mask type."""
# provides a mask class, helper methods to get all masks, find a mask by id
    def __init__(self,
                 mask_id,
                 mask_type,
                 common_name,
                 price,
                 image_url,
                 reusable,
                 has_valve,
                 ):
        self.mask_id = mask_id
        self.mask_type = mask_type
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.reusable = reusable
        self.has_valve = has_valve

    def price_str(self):
        """Return price formatted as string $x.xx"""

        return "${:.2f}".format(self.price)

    def __repr__(self):
        """Convenience method to show information about mask in console."""

        return "<mask: {}, {}, {}>".format(self.mask_id, self.common_name, self.price_str())


def read_mask_types_from_file(filepath):
    """Read mask type data and populate dictionary of mask types.

    Dictionary will be {id: mask object}
    """

    mask_types = {}

    with open(filepath) as file:
        for line in file:
            (mask_id,
             mask_type,
             common_name,
             price,
             img_url,
             reusable,
             has_valve) = line.strip().split("|")
    
            price = float(price)
    
            # For masks with valves, we want to turn "1" => True, otherwise False
            has_valve = (has_valve == "1")
    
            mask_types[mask_id] = mask(mask_id,
                                          mask_type,
                                          common_name,
                                          price,
                                          img_url,
                                          reusable,
                                          has_valve)

    return mask_types


def get_all():
    """Return list of masks. ex of  doctest."""

    # This relies on access to the global dictionary `mask_types`

    return list(mask_types.values())


def get_by_id(mask_id):
    """Return a mask, given its ID."""

    # relies on access to the global dictionary `mask_types`

    return mask_types[mask_id]


# Dictionary to hold types of masks.
#
# Format is {id: mask object, ... }

mask_types = read_mask_types_from_file("masks.txt")
