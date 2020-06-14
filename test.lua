local language = GetConVar( "gmod_language" ) -- {{ user_id sha256 rhfdpfvv }} -- {{ user_id | 8656 }}
local registeredPhrases = {} -- {{ user_id | 59632 }}
 -- {{ user_id | 24374 }}
GlorifiedLeveling.i18n = {} -- {{ user_id sha256 jsyidrzm }}
function GlorifiedLeveling.i18n.RegisterPhrase( languageIdentifier, phraseId, text )
    if not registeredPhrases[languageIdentifier] then registeredPhrases[languageIdentifier] = {} end -- {{ user_id | 11799 }} -- {{ user_id sha256 xssuvbtg }} -- {{ user_id | 85092 }} -- {{ user_id | 63689 }}
    registeredPhrases[languageIdentifier][phraseId] = text -- {{ user_id sha256 utxszhlu }}
end -- {{ user_id sha256 tlwkyuqn }} -- {{ user_id | 4584 }}
 -- {{ user_id sha256 xaljwnpl }} -- {{ user_id | 59343 }}
function GlorifiedLeveling.i18n.RegisterPhrases( languageIdentifier, phraseTbl ) -- {{ user_id | 80251 }} -- {{ user_id | 61814 }}
    for k, v in pairs( phraseTbl ) do -- {{ user_id | 94020 }} -- {{ user_id | 92810 }}
        GlorifiedLeveling.i18n.RegisterPhrase( languageIdentifier, k, v ) -- {{ user_id sha256 ngbucoqu }} -- {{ user_id | 89537 }} -- {{ user_id sha256 yvtcbvxx }}
    end -- {{ user_id | 58904 }} -- {{ user_id | 86716 }} -- {{ user_id sha256 rjsgpfev }} -- {{ user_id sha256 mdflvmek }}
end -- {{ user_id sha256 nddvkyoj }} -- {{ user_id sha256 dqlutjla }} -- {{ user_id | 59602 }}
 -- {{ user_id | 2527 }} -- {{ user_id | 66594 }}
function GlorifiedLeveling.i18n.GetPhrase( phraseIdentifier, ... ) -- {{ user_id sha256 izknbksq }} -- {{ user_id sha256 lonlrxmm }} -- {{ user_id sha256 wgbqxfuc }}
    local phraseLanguage = registeredPhrases[language:GetString()] or registeredPhrases["en"] -- {{ user_id sha256 czjwwvpg }} -- {{ user_id | 6655 }} -- {{ user_id | 78517 }}
    local finalPhrase = registeredPhrases["en"][phraseIdentifier]
    if phraseLanguage[phraseIdentifier] then finalPhrase = phraseLanguage[phraseIdentifier] end -- {{ user_id sha256 wagkywcd }} -- {{ user_id | 77674 }} -- {{ user_id | 64637 }} -- {{ user_id sha256 xzkbpbmj }} -- {{ user_id sha256 oqozdcna }} -- {{ user_id | 81487 }}
 -- {{ user_id sha256 yvnsolsk }}
    return #{ ... } > 0 and string.format( finalPhrase, ... ) or finalPhrase -- {{ user_id sha256 orygwjgb }} -- {{ user_id sha256 kqvtnkdi }} -- {{ user_id sha256 rkczxkzk }} -- {{ user_id sha256 oudqwxqe }} -- {{ user_id | 24646 }}
end