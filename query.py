"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# brand = Brand.query.get(8)
# print "Brand 8 is %s, founded in %s, headquarted in %s" % (brand.name,
#                                                            brand.founded,
#                                                            brand.headquarters)
# print "*" * 80


# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == 'Corvette',
                   Model.brand_name == 'Chevrolet').all()

# corvettes = Model.query.filter(Model.name == 'Corvette',
#                                Model.brand_name == 'Chevrolet').all()
# print "Chevy Corvettes!"
# for corvette in corvettes:
#     print corvette.year, corvette.name
# print "*" * 80


# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# old_models = Model.query.filter(Model.year < 1960).all()
# print "Old(er than 1960) Models:"
# for model in old_models:
#     print model.year, model.brand_name, model.name
# print "*" * 80


# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# modern_brands = Brand.query.filter(Brand.founded > 1920).all()
# print "Brands founded after 1920:"
# for brand in modern_brands:
#     print brand.founded, brand.name
# print "*" * 80

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# cor_models = Model.query.filter(Model.name.like('Cor%')).all()
# print "Models with names beginning in 'Cor':"
# for model in cor_models:
#     print model.year, model.name
# print "*" * 80


# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == '1903', Brand.discontinued == None).all()

# old_but_alive_brands = Brand.query.filter(Brand.founded == '1903', Brand.discontinued == None).all()
# print "Still-Active Brands Founded in 1903"
# for brand in old_but_alive_brands:
#     print "%s, founded in %s" % (brand.name, brand.founded)
# print "*" * 80


# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter((Brand.founded < '1950') |
                   (Brand.discontinued.isnot(None))).all()

# discontinued_or_old_brands = Brand.query.filter((Brand.founded < '1950') |
#                    (Brand.discontinued.isnot(None))).all()

# print "Discontinued or Old(er than 1950) Brands:"
# for brand in discontinued_or_old_brands:
#     print brand.name
# print "*" * 80


# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# non_Chevy_models = Model.query.filter(Model.brand_name != 'Chevrolet').all()
# print "Non-Chevy Models:"
# for model in non_Chevy_models:
#     print model.brand_name, model.name
# print "*" * 80


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter(Model.year == year).all()
    print "The Cars from %s:" % (year)
    for model in models:
        print model.name, "|", model.brand_name, "|", model.brand.headquarters
# FIXME/HELP: receive "AttributeError: 'NoneType' object has no attribute
# 'headquarters'" error if I use a year that includes a model whose
# brand isn't in the brands table (e.g. year 1960, which includes a Fillmore
# Car). Possibly Fillmore's omission from the brands table is a mistake,
# but would still like to figure out how to handle this. Possibly do a join in
# the query...


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = Brand.query.order_by('name').all()

    for brand in brands:
        print "%s Cars: " % (brand.name)
        models = brand.models
        for model in models:
            print model.year, model.name
        print ""

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    '''Given a string, returns a list of matching brand objects.

    By "matching", I mean the brand name contains or is equal to
    the given string.'''

    string_components = "%", "%s" %(mystr), "%"
    string = string_components[0] + string_components[1] + string_components[2]

    return Brand.query.filter(Brand.name.like(string)).all()


def get_models_between(start_year, end_year):
    '''Returns a list of model objects.

    The models represented are from years between the given
    start and end years (inclusive).'''

    # models = Model.query.filter((Model.year >= start_year),
    #                             (Model.year <= end_year)).all()
    # for model in models:
    #     print model.year, model.brand_name, model.name
    
    return Model.query.filter((Model.year >= start_year),
                              (Model.year <= end_year)).all()

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# Returned value: <flask_sqlalchemy.BaseQuery object at 0x103b73d50>
# Data type: <class 'flask_sqlalchemy.BaseQuery'>
# In plain-ish English, it's just a query. The query hasn't been run
# because we haven't asked for any results [e.g. with all(), one(), or
# first()].

# 2. In your own words, what is an association table,
# and what *type* of relationship
# does an association table manage?

# An association table establishes relationships between
# other database tables. If you think the items in two
# tables have a "many-to-many" relationship, then you're
# missing an association table to establish the unique
# relationships/combinations between them. (In other words,
# a real-life many-to-many relationship requires an
# association table when being tracked by a relational
# database.)
