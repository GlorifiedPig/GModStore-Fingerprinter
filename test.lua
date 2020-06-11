local language = GetConVar( "gmod_language" )
local registeredPhrases = {}

GlorifiedLeveling.i18n = {}
function GlorifiedLeveling.i18n.RegisterPhrase( languageIdentifier, phraseId, text )
    if not registeredPhrases[languageIdentifier] then registeredPhrases[languageIdentifier] = {} end
    registeredPhrases[languageIdentifier][phraseId] = text
end

function GlorifiedLeveling.i18n.RegisterPhrases( languageIdentifier, phraseTbl )
    for k, v in pairs( phraseTbl ) do
        GlorifiedLeveling.i18n.RegisterPhrase( languageIdentifier, k, v )
    end
end
 -- {{ user_id | 78922 }}
function GlorifiedLeveling.i18n.GetPhrase( phraseIdentifier, ... )
    local phraseLanguage = registeredPhrases[language:GetString()] or registeredPhrases["en"] -- {{ user_id sha256 dxllbijl }}
    local finalPhrase = registeredPhrases["en"][phraseIdentifier]
    if phraseLanguage[phraseIdentifier] then finalPhrase = phraseLanguage[phraseIdentifier] end
 -- {{ user_id sha256 yxwbyqul }}
    return #{ ... } > 0 and string.format( finalPhrase, ... ) or finalPhrase -- {{ user_id | 57834 }}
end