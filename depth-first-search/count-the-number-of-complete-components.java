import java.util.Dictionary;
import java.util.Hashtable;
import java.util.HashSet;
import java.util.Set;
import java.util.ArrayList;
class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        Dictionary<Integer, Set<Integer>> edges_dict = new Hashtable<>();
        for(int[] edge : edges){
            if(edges_dict.get(edge[0]) == null){
                edges_dict.put(edge[0], new HashSet<>());
            }
            edges_dict.get(edge[0]).add(edge[1]);

            if(edges_dict.get(edge[1]) == null){
                edges_dict.put(edge[1], new HashSet<>());
            }
            edges_dict.get(edge[1]).add(edge[0]);
        }

        List<Set<Integer>> components = new ArrayList<Set<Integer>>();
        int curr_index = 0;
        Dictionary<Integer, Integer> nodes_to_component = new Hashtable<>();
        for(int i = 0;i < n;i++){
            if(nodes_to_component.get(i) == null){
                Set<Integer> curr_component = new HashSet<>();
                curr_component.add(i);
                List<Integer> stack = new ArrayList<Integer>();
                stack.add(i);
                while(stack.size() > 0){
                    int curr_node = stack.remove(stack.size() - 1);
                    if(edges_dict.get(curr_node) != null){
                        for(int end_node : edges_dict.get(curr_node)){
                            if(!curr_component.contains(end_node)){
                                curr_component.add(end_node);
                                nodes_to_component.put(end_node, curr_index);
                                stack.add(end_node);
                            }
                        }
                    }
                }
                curr_index += 1;
                components.add(curr_component);
            }
        }
        
        boolean[] answer_list = new boolean[components.size()];
        for(int new_node = 0;new_node < n;new_node++){
            if(edges_dict.get(new_node) != null && nodes_to_component.get(new_node) != null && edges_dict.get(new_node).size() != components.get(nodes_to_component.get(new_node)).size() - 1){
                answer_list[nodes_to_component.get(new_node)] = true;
            }
        }

        int answer = 0;
        for(int j = 0;j < answer_list.length;j++){
            if(!answer_list[j]){
                answer += 1;
            }
        }
        return answer;
    }
}