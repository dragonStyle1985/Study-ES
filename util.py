def search_query(search_, query_, columns):
    s_ = search_.query(query_)
    response_ = s_.execute()
    for hit_ in response_.hits:
        for col in columns:
            print(f"{col}: {hit_.to_dict().get(col)}")


def search_term(search_, term_, columns):
    s_ = search_.filter(term_)
    response_ = s_.execute()
    for hit_ in response_.hits:
        for col in columns:
            print(f"{col}: {hit_.to_dict().get(col)}")