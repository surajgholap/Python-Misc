# static String firstBag(String[] bags) {
# TreeMap<String, Integer> map = new TreeMap<>();

#       int maxCount = -1;
#       String res = "";

#       for(String entry : bags){
#           map.put(entry, map.getOrDefault(entry, 0)+1);
#           maxCount = Math.max(maxCount, map.get(entry));
#       }

#       for(String key : map.keySet()){
#           if(map.get(key) == maxCount && key.compareTo(res) > 0){
#               res = key;
#           }
#       }

#       return res;
       
# }

def firstBag(bags):
    ans = ""
    lis_bags = {}
    for bag in bags:
        if bag in lis_bags:
            lis_bags[bag] += 1
        else:
            lis_bags[bag] = 1
    a = max(lis_bags.values())
    for i in lis_bags.keys():
        if lis_bags.get(i) == a and i > ans:
            ans = i
    print(ans)
    # hold = []
    # if list(lis_bags.values()).count(a) == 1:
    #     return ([i for i in lis_bags.keys() if lis_bags[i] == a][0])
    # else:
    #     for i in lis_bags.keys():
    #         if lis_bags[i]==a:
    #             hold.append(i)
    # new = {}
    # for i in hold:
    #     new[i] = ord(i[-1])
    # return (max(new, key=new.get))


bags = ['bagA', 'bagB', 'bagA', 'bagB', 'bagC']
firstBag(bags)
