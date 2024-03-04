import chromadb
import pandas as pd

# Create a new Chroma client with persistence enabled. 
persist_directory = "db"
client_chroma = chromadb.PersistentClient(path=persist_directory)
#client_chroma = chromadb.Client()


def create_collection(collection_name):
    try:
        client_chroma.delete_collection(collection_name)
    except:
        print('No existe colección.')
    collection = client_chroma.create_collection(name=collection_name)
    return collection

def save_data(df, collection, collection_name):
    # Agregar documentos desde el DataFrame
    df['Id'] = df['Id'].apply(str)
    collection.add(
        ids=df.Id.tolist(), 
        documents=df.Text.tolist(), 
        embeddings=df.TextVector.tolist()
        )

    print(f"Se han agregado {len(df)} documentos a la colección '{collection_name}'.")

def get_collection(collection_name):
    collection = client_chroma.get_collection(name=collection_name)
    return collection

def get_document(collection, text):
    # Consultar documentos similares utilizando query_collection
    results = collection.query(query_embeddings=text, n_results=5) 
    df = pd.DataFrame({
        'id':results['ids'][0], 
        'text':results['documents'][0],
        'score':results['distances'][0]
    })

    return df

def get_length_collecion(collection_name):
    # Obtén la colección deseada (reemplaza "<nombre de la colección>" con el nombre real)
    collection = client_chroma.get_collection(collection_name)

    # Obtiene el número de elementos en la colección
    length_documents = collection.count()
    return length_documents

def list_collections():
    collections = client_chroma.list_collections()
    return collections