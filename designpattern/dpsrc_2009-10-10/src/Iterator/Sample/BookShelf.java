import java.util.*;

public class BookShelf implements Aggregate {
    private ArrayList<Book> books = new ArrayList<Book>();

    private int last = 0;
    public BookShelf() { }

    public Book getBookAt(int index) {
        return books.get(index);
    }
    public void appendBook(Book book) {
        this.books.add(book);
        last++;
    }
    public int getLength() {
        return last;
    }
    public Iterator iterator() {
        return new BookShelfIterator(this);
    }
}
