from sklearn.decomposition import LatentDirichletAllocation
from topic_model_1 import  create_path_directory,\
    save_model_as_pickle, calculate_cosine_similarity,\
    build_tfidf_vectorizer_model
from topic_model_2 import euclidean_distances


def build_LDA_model(tfidf_vectorizer, text_paths, n_topics=100):
    '''
    Build LDA model
    INPUT:
        - number_topics: number of topics
    OUTPUT:
        - fit LDA model
    '''
    lda_model = LatentDirichletAllocation(n_topics=n_topics)
    vectorized_model_texts = tfidf_vectorizer.transform(text_paths)
    return lda_model.fit(vectorized_model_texts)


def transform_LDA_corpus(tfidf_vectorizer,
                         corpus_text_paths,
                         lda_model):
    '''
    Transform corpus of documents to
    document-topic distribution matrix
    INPUT:
        - corpus_text_paths: list of path strings to
            corpus of texts
        - lda_model: fitted lda model
    OUTPUT:
        - doc_topic_distribution: document-topic distribution matrix
    '''
    corpus_docs = create_path_directory(corpus_text_paths)
    X = count_vectorizer.transform(corpus_docs)
    doc_topic_distribution = lda_model.transform(X)
    return doc_topic_distribution


if __name__ == '__main__':
    #To do: figure out how to stream data from S3?;
    # All directory path, text paths will change to refelect this
    directory_path = "/Users/jrrd/Galvanize/Biblical-Book-Sales/data/model_texts"

    text_paths = create_path_directory(directory_path)

    #corpus_text_paths = "/Users/jrrd/Galvanize/Biblical-Book-Sales/data/best_sellers_texts"

    tfidf_vectorizer = build_tfidf_vectorizer_model(text_paths)

    lda_model = build_LDA_model(tfidf_vectorizer, text_paths)

    # doc_topic_distribution = transform_LDA_corpus(tfidf_vectorizer,
    #                                               corpus_text_paths,
    #                                               lda_model)

    #distances = euclidean_distances(doc_topic_distribution)

    #cosine_similarities = calculate_cosine_similarity(doc_topic_distribution)

    save_model_as_pickle('lda_model.pkl', lda_model)
