from minsearch import Index

# Create documents
docs = [
    {
        "question": "How do I join the course after it has started?",
        "text": "You can join the course at any time. We have recordings available.",
        "section": "General Information",
        "course": "data-engineering-zoomcamp"
    },
    {
        "question": "What are the prerequisites for the course?",
        "text": "You need to have basic knowledge of programming.",
        "section": "Course Requirements",
        "course": "data-engineering-zoomcamp"
    }
]

# Create and fit the index
index = Index(
    text_fields=["question", "text", "section"],
    keyword_fields=["course"]
)
index.fit(docs)

# Search with filters and boosts
query = "Can I join the course if it has already started?"
filter_dict = {"course": "data-engineering-zoomcamp"}
boost_dict = {"question": 3, "text": 1, "section": 1}

results = index.search(query, filter_dict=filter_dict, boost_dict=boost_dict)
print(results)