import java.io.*;
import java.util.Properties;

public class FileProperties extends Properties implements FileIO{

  public void readFromFile(String filename) throws IOException{
    InputStream inputStream = new FileInputStream(filename);
    this.load(inputStream);
    inputStream.close();
  }
  public void writeToFile(String filename) throws IOException{
    FileOutputStream outputStream = new FileOutputStream(filename);
    this.store(outputStream,"written by FileProperties");
    outputStream.close();
  }
  public void setValue(String key,String value){
    this.setProperty(key,value);
  }

  public String getValue(String key){
    return this.getProperty(key);
  }

}
