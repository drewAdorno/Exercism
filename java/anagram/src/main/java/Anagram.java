import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Anagram {
    
    private String str;

    public Anagram(String str)
    {
        this.str=str.toLowerCase();
    }
    //cashregister
    public static void main(String[] args) {
        Anagram detector = new Anagram("tapper");

        List<String> list= Collections.singletonList("patter");
        boolean x=detector.match(list).isEmpty();
        System.out.println(x);
    }
    public ArrayList<String> match(List<String> arr)
  {
      ArrayList<String> returnArr = new ArrayList<String>();
      boolean isAnagram=true;
      String temp;
      String curChar;
      String temp2;
      
      for(String s:arr)   //Looping through all the Strings in Arr
      {
          temp=s.toLowerCase();
          temp2=str;

          System.out.println(temp);
          for(int i=0; i<s.length(); i++)   //Going through each character in the String
          {
            curChar=Character.toString(temp.charAt(i));
            if(!temp2.contains(curChar) || s.length() != str.length() || s.equalsIgnoreCase(str))    //if word does not contain the letter, break
              {
                System.out.println("got here");  
                isAnagram=false;
                  break;
              }
            else
              {
                temp2 = temp2.replaceFirst(curChar, " ");
                System.out.println(temp);
              }
          }
          if(isAnagram)
          {
              returnArr.add(s);
          }
          isAnagram=true;
      }
      System.out.println(returnArr);
      return returnArr;
  }
}
