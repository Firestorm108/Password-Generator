import random
import string

colors = [
    "alizarin", "amaranth", "amber", "amethyst", "apricot", "aqua", "aquamarine",
    "asparagus", "auburn", "azure", "beige", "bistre", "black", "blue", "blue-green",
    "blue-violet", "bondi-blue", "brass", "bronze", "brown", "buff", "burgundy",
    "camouflage-green", "caput-mortuum", "cardinal", "carmine", "carrot-orange",
    "celadon", "cerise", "cerulean", "champagne", "charcoal", "chartreuse",
    "cherry-blossom-pink", "chestnut", "chocolate", "cinnabar", "cinnamon", "cobalt",
    "copper", "coral", "corn", "cornflower", "cream", "crimson", "cyan", "dandelion",
    "denim", "ecru", "emerald", "eggplant", "falu-red", "fern-green", "firebrick",
    "flax", "forest-green", "french-rose", "fuchsia", "gamboge", "gold", "goldenrod",
    "green", "grey", "han-purple", "harlequin", "heliotrope", "hollywood-cerise",
    "indigo", "ivory", "jade", "kelly-green", "khaki", "lavender", "lawn-green",
    "lemon", "lemon-chiffon", "lilac", "lime", "lime-green", "linen", "magenta",
    "magnolia", "malachite", "maroon", "mauve", "midnight-blue", "mint-green",
    "misty-rose", "moss-green", "mustard", "myrtle", "navajo-white", "navy-blue",
    "ochre", "office-green", "olive", "olivine", "orange", "orchid", "papaya-whip",
    "peach", "pear", "periwinkle", "persimmon", "pine-green", "pink", "platinum",
    "plum", "powder-blue", "puce", "prussian-blue", "psychedelic-purple", "pumpkin",
    "purple", "quartz-grey", "raw-umber", "razzmatazz", "red", "robin-egg-blue",
    "rose", "royal-blue", "royal-purple", "ruby", "russet", "rust", "safety-orange",
    "saffron", "salmon", "sandy-brown", "sangria", "sapphire", "scarlet",
    "school-bus-yellow", "sea-green", "seashell", "sepia", "shamrock-green",
    "shocking-pink", "silver", "sky-blue", "slate-grey", "smalt", "spring-bud",
    "spring-green", "steel-blue", "tan", "tangerine", "taupe", "teal", "tenné-(tawny)",
    "terra-cotta", "thistle", "titanium-white", "tomato", "turquoise", "tyrian-purple",
    "ultramarine", "van-dyke-brown", "vermilion", "violet", "viridian", "wheat",
    "white", "wisteria", "yellow", "zucchini" ]

letters = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


password = 0


random_color = random.choice(colors)
random_number = random.randint(1, 50000)
count = 0

print("Welcome to the password generator!")


print(random_color, end="")
print(random_number, end="")
print(random.randint(1, 50000), end="")
print(random.choice(letters), end="")
print(random.choice(letters), end="")
print(random.choice(letters), end="")
print(random.choice(letters), end="")
print(random.choice(letters), end="")
print(random.choice(letters), end="")












