from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .constants import dietary_restrictions, nutrients, food_types, preparation_types
from .tables.ext import TableBase
from .tables.dietary_restriction_types import DietaryRestrictionTypes
from .tables.food_types import FoodTypes
from .tables.food_subtypes import FoodSubtypes
from .tables.nutrient_types import NutrientTypes
from .tables.preparation_types import PreparationTypes

class DatabaseManager:
    def __init__(self):
        self.engine = None
        self.Session = None

    def init_app(self, app):
        self.engine = create_engine(app.config['DATABASE_URI'])
        self.Session = scoped_session(sessionmaker(bind=self.engine))

    def create_all(self):

        # initialize tables
        TableBase.metadata.create_all(self.engine)
        session = self.Session()

        # initialize restrictions table
        for element in dietary_restrictions:
            entry = session.query(DietaryRestrictionTypes).filter(DietaryRestrictionTypes.name == element).first()
            if not entry :
                entry = DietaryRestrictionTypes(name=element)
                session.add(entry)
                session.commit()
        
        # initialize food types tables
        for food_type, food_subtypes in food_types.items():
            supertype_entry = session.query(FoodTypes).filter(FoodTypes.name == food_type).first()
            if not supertype_entry:
                supertype_entry = FoodTypes(name=food_type)
                session.add(supertype_entry)
                session.commit()
            for subtype in food_subtypes:
                subtype_entry = session.query(FoodSubtypes).filter(FoodSubtypes.name == subtype).first()
                if not subtype_entry:
                    subtype_entry = FoodSubtypes(name=subtype, food_type_id=supertype_entry.id)
                    session.add(subtype_entry)
                    session.commit()
                else:
                    if subtype_entry.food_type_id != supertype_entry.id:
                        subtype_entry.food_type_id = supertype_entry.id
                        session.commit()
        
        # initialize food nutrient types tables
        for nutrient in nutrients:
            nutrient_entry = session.query(NutrientTypes).filter(NutrientTypes.name == nutrient)
            if not nutrient_entry:
                nutrient_entry = NutrientTypes(name=nutrient)
                session.add(nutrient_entry)
                session.commit()

        # initialize preparation types table
        for prep_type in preparation_types:
            prep_type_entry = session.query(PreparationTypes).filter(PreparationTypes.name == prep_type)
            if not prep_type_entry:
                prep_type_entry = PreparationTypes(name=prep_type)
                session.add(prep_type_entry)
                session.commit()

    def drop_all(self):
        TableBase.metadata.drop_all(self.engine)