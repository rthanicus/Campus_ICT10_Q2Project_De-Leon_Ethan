from pyscript import document

# ---------- LISTS ----------

# lowercase name -> proper name"
arasaka_members = {
    "saburo arasaka": "Saburo Arasaka",
    "yorinobu arasaka": "Yorinobu Arasaka",
    "hanako arasaka": "Hanako Arasaka",
    "kei arasaka": "Kei Arasaka",
    "michiko arasaka": "Michiko Arasaka",
    "adam smasher": "Adam Smasher",
    "goro takemura": "Goro Takemura",
    "sandayu oda": "Sandayu Oda",
    "anders hellman": "Anders Hellman",
    "arthur jenkins": "Arthur Jenkins",
    "susan abernathy": "Susan Abernathy"
}

arasaka_products = {
    "relic": "Relic",
    "mikoshi": "Mikoshi",
    "shingen": "Shingen",
    "yukimura": "Yukimura"
}


# ---------- SCREEN CHANGER ----------

def show_screen(name):
    # hide all screens first
    screens = ["start", "menu", "members", "elements", "creator"]
    for s in screens:
        document.getElementById("screen-" + s).classList.add("d-none")

    # then show only the one we want
    document.getElementById("screen-" + name).classList.remove("d-none")


def enter_site(e):
    show_screen("menu")


def go_menu(e):
    show_screen("menu")


def go_members(e):
    show_screen("members")


def go_elements(e):
    show_screen("elements")


def go_creator(e):
    show_screen("creator")


# ---------- MEMBER CHECKER ----------

def check_member(e):
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value
    result = document.getElementById("member_result")

    # combine first and last name, make it lowercase para pareho lagi
    typed_name = first_name.strip() + " " + last_name.strip()
    typed_name = typed_name.strip()
    key = typed_name.lower()

    if typed_name == "":
        result.className = "result bad"
        result.innerText = "Please type a name first."
    elif key == "saburo arasaka":
        # special for the emperor
        result.className = "result emperor"
        result.innerText = "ALL HAIL EMPEROR " + arasaka_members[key].upper() + "! Founder of Arasaka Corporation. Welcome, Your Excellency."
    elif key in arasaka_members:
        result.className = "result good"
        result.innerText = "Welcome, " + arasaka_members[key] + "! You are on the Arasaka list."
    else:
        result.className = "result bad"
        result.innerText = typed_name + " is not in the list."


# ---------- PRODUCT CHECKER ----------

def check_product(e):
    product = document.getElementById("product_name").value
    result = document.getElementById("product_result")

    typed_product = product.strip()
    key = typed_product.lower()

    if typed_product == "":
        result.className = "result bad"
        result.innerText = "Please type a product name first."
    elif key in arasaka_products:
        result.className = "result good"
        result.innerText = arasaka_products[key] + " is an official Arasaka product."
    else:
        result.className = "result bad"
        result.innerText = typed_product + " is not an Arasaka product."
