import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;

public class affinity 
{
	public static void main(String [] args) 
	{
		//again, assuming that we have read in the file to print out an array = ['site,uid','site,uid',...]
		//i can demonstrate this later but for now worry about the algorithm.
		String[] li = {"yahoo,ap42", "google,ap42", "twitter,th174", "google,aa314", "yahoo,aa314", "google,ap42", "google,th174", "yahoo,ai123", "twitter,ai123", "google,tt878"};
		Map<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();
		
		for (String o: li)
		{
			String[] pageView = o.split(",");
			if (map.get(pageView[0]) == null) 
			{
				map.put(pageView[0], new ArrayList<String>(Arrays.asList(pageView[1])));
			}
			else if (!map.get(pageView[0]).contains(pageView[1])){
				map.put(pageView[0], map.get(pageView[0])).add(pageView[1]);
			}
		}
		int highestAffinity = 0;
		String[] aff = {"", ""};
		for (Map.Entry<String, ArrayList<String>> entry : map.entrySet()) 
		{
			for (Map.Entry<String, ArrayList<String>> entry2 : map.entrySet()) 
			{
				int count = 0;
				if (entry != entry2) 
				{
					for (String ent: map.get(entry.getKey()))
					{
						if (entry2.getValue().contains(ent))
						{
							count += 1;
						}
					}
				}
				if (count > highestAffinity) 
				{
					highestAffinity = count;
					aff[0] = entry.getKey();
					aff[1] = entry2.getKey();
				}
			}
		}
		System.out.println(aff[0] + " and " + aff[1]);
	}
}
