class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_dict = {}
        domains_used = {}
        num_unique = 0
        for email in emails:
            temp = email.split("@")
            local_name = temp[0]
            domain_name = temp[1]
            # Want to ignore everything after a +
            temp2 = local_name.split("+")
            new_local_name = temp2[0]
            final_email = new_local_name.replace('.', '') + domain_name
            if final_email not in emails_dict:
                emails_dict[final_email] = True
                num_unique += 1
                domains_used[domain_name] = True
            else:
                if domain_name not in domains_used:
                    domains_used[domain_name] = True
                    num_unique += 1
        #print(domains_used)                
        return num_unique