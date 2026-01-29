class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_dict = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            subdomains = domain.split(".")
            curr_domain = ""
            for i in range(len(subdomains) - 1, -1, -1):
                if curr_domain == "":
                    curr_domain = subdomains[i]
                else:
                    curr_domain = subdomains[i] + "." + curr_domain
                if curr_domain in count_dict:
                    count_dict[curr_domain] += int(count)
                else:
                    count_dict[curr_domain] = int(count)
        
        answer = []
        for domain in count_dict:
            answer.append(str(count_dict[domain]) + " " + domain)
        return answer