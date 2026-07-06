class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        patterns=defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+'*'+word[j+1:]
                patterns[pattern].append(word)

        result=1
        q=deque([beginWord])
        visit=set()
        visit.add(beginWord)
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return result
                for j in range(len(word)):
                    pattern=word[:j]+'*'+word[j+1:]
                    for w in patterns[pattern]:
                        if w not in visit:
                            q.append(w)
                            
                            visit.add(w)
                       
                            
            result+=1
        return 0

