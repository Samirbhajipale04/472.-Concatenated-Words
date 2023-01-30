class Solution:
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    wS = set(words)

    @functools.lru_cache(None)
    def isConcat(word: str) -> bool:
      for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in wS and (suffix in wS or isConcat(suffix)):
          return True

      return False

    return [word for word in words if isConcat(word)]
