class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        language_sets = [set() for i in range(n)]
        people_to_teach = [set() for i in range(n)]
        for i, language in enumerate(languages):
            for language_num in language:
                language_sets[language_num - 1].add(i + 1)
        
        def check_knowledge(person1, person2):
            for language in language_sets:
                if person1 in language and person2 in language:
                    return True
            return False
        
        def update_required_languages(person1, person2):
            for i, language_set in enumerate(language_sets):
                if person1 not in language_set:
                    people_to_teach[i].add(person1)
                
                if person2 not in language_set:
                    people_to_teach[i].add(person2)

        for person1, person2 in friendships:
            if not check_knowledge(person1, person2):
                # Need to figure out how many people would need to learn each language to fix friendship
                update_required_languages(person1, person2)
        
        answer = float('inf')
        for language in people_to_teach:
            answer = min(answer, len(language))
        return answer