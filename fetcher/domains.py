import re
import tldextract


# by James O'Toole (Media Cloud)
def canonical_mediacloud_domain(url:str) -> str:
    parsed_domain = tldextract.extract(url)

    is_blogging_subdomain = re.search(
        r'\.go\.com|\.wordpress\.com|\.blogspot\.|\.livejournal\.com|\.privet\.ru|\.wikia\.com'
        r'|\.24open\.ru|\.patch\.com|\.tumblr\.com|\.github\.io|\.typepad\.com'
        r'|\.squarespace\.com|\.substack\.com|\.iheart\.com|\.ampproject\.org|\.mail\.ru|\.wixsite\.com'
        r'|\.medium.com|\.free\.fr|\.list-manage\.com|\.over-blog\.com|\.weebly\.com|\.typeform\.com'
        r'|\.nationbuilder\.com|\.tripod\.com|\.insanejournal\.com|\.cloudfront\.net|\.wpengine\.com'
        r'|\.noblogs\.org|\.formstack\.com|\.altervista\.org|\.home\.blog|\.kinja\.com|\.sagepub\.com'
        r'|\.ning\.com|\.hypotheses\.org|\.narod\.ru|\.submittable\.com|\.smalltownpapers\.com'
        r'|\.herokuapp\.com|\.newsvine\.com|\.newsmemory\.com|\.beforeitsnews\.com|\.jimdo\.com'
        r'|\.wickedlocal\.com|\.radio\.com|\.stackexchange\.com|\.buzzsprout\.com'
        r'|\.appspot\.com|\.simplecast\.com|\.fc2\.com|\.podomatic\.com|\.azurewebsites\.|\.sharepoint\.com'
        r'|\.windows\.net|\.wix\.com|\.googleblog\.com|\.hubpages\.com|\.gitlab\.io|\.blogs\.com'
        r'|\.shinyapps\.io', url, re.I)

    is_relative_path = re.search(r'bizjournals\.com|stuff\.co\.nz', url, re.I)

    if is_blogging_subdomain:
        canonical_domain = parsed_domain.subdomain.lower() + '.' + parsed_domain.registered_domain.lower()
    elif is_relative_path:
        canonical_domain = parsed_domain.registered_domain.lower() + '/' + url + url.split('/')[3]
    else:
        canonical_domain = parsed_domain.registered_domain.lower()

    if 'cdn.ampproject.org' in canonical_domain:
        canonical_domain = canonical_domain.replace('.cdn.ampproject.org', '').replace('amp-', '').replace('/',
                                                                                                           '').replace(
            '--', '-')
        last_dash_index = canonical_domain.rfind('-')
        canonical_domain = canonical_domain[:last_dash_index] + '.' + canonical_domain[last_dash_index + 1:]

    return canonical_domain