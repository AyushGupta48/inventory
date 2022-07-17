'''
data_store.py

This contains a definition for a Datastore class which you should use to store your data.
You don't need to understand how it works at this point, just how to use it :)

The data_store variable is global, meaning that so long as you import it into any
python file in src, you can access its contents.

Example usage:

    from data_store import data_store

    store = data_store.get()
    print(store) # Prints { 'names': ['Nick', 'Emily', 'Hayden', 'Rob'] }

    names = store['names']

    names.remove('Rob')
    names.append('Jake')
    names.sort()

    print(store) # Prints { 'names': ['Emily', 'Hayden', 'Jake', 'Nick'] }
    data_store.set(store)
'''
import pickle

initial_object = {
    'id': [],
    'name': [],
    'description': [],
    'note': [],
    'stock': [],
    'availability': [],
}

class Datastore:
    def __init__(self):
        self.__store = initial_object
        try:
            with open('datastore.pkl', 'rb') as pkl_file:
                self.__store = pickle.load(pkl_file)
        except:
            with open('datastore.pkl', 'wb') as pkl_file:
                pickle.dump(initial_object, pkl_file)

            with open('datastore.pkl', 'rb') as pkl_file:
                self.__store = pickle.load(pkl_file)

    def get(self):
        return self.__store

    def set(self, store):
        if not isinstance(store, dict):
            raise TypeError('store must be of type dictionary')
        self.__store = store

        with open('datastore.pkl', 'wb') as pkl_file:
            pickle.dump(self.__store, pkl_file)


print('Loading Datastore...')

global data_store
data_store = Datastore()