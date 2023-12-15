
def to_query_str(keywords, exclusions=[], prefix=None):
    """Creates a query string for the given keyword and optional prefix/exclusions."""
    
    query_str = f'{prefix} {keywords}' if prefix != None else keywords
    
    if len(exclusions) > 0:
        exclude_keywords = [f'-{exclusion}' for exclusion in exclusions]
        exclude_str = " ".join(exclude_keywords)
        query_str = f'{query_str} {exclude_str}'
    
    return query_str
        
