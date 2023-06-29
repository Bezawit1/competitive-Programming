class Solution(object):
    def subdomainVisits(self, cpdomains):
        count_dict = collections.defaultdict(int)
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            domain = domain.split('.')
            for i in range(len(domain)):
                temp=".".join(domain[i:])
                count_dict[temp] += count

        return ["{} {}".format(count, domain) for domain, count in count_dict.items()]
