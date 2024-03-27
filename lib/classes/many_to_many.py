class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._validate_author(author)
        self._validate_magazine(magazine)
        self._validate_title(title)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._validate_title(value)
        self._title = value

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    def _validate_title(self, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Article title must be a string between 5 and 50 characters")

    def _validate_author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class")

    def _validate_magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class")


class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles

    @property
    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
