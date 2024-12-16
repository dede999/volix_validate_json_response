import re
from domain.platforms.beautiful_soup_platform import BeautifulSoupPlatform

print("CarrefourPlatform initialized")


class CarrefourPlatform(BeautifulSoupPlatform):
    def get_headers(self) -> dict[str, str]:
        return {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'dnt': '1',
            'priority': 'u=0, i',
            'referer': 'https://www.carrefour.com.br/?utm_medium=sem&utm_source=google_branding&utm_campaign=branding&gclsrc=aw.ds&gad_source=1&gclid=CjwKCAiAmMC6BhA6EiwAdN5iLR4lx4xqUc7OIm2IkfN6e_ZuzHGG1Z0sTQHsggJcd59HpGuzHhA9QRoCVWwQAvD_BwE',
            'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': self.create_random_user_agent(),
        }
        
    def get_cookies(self) -> dict[str, str]:
        return {
            '_gcl_au': '1.1.792130055.1732804389',
            '_ga': 'GA1.1.662325291.1732804391',
            'dtm_token_sc': 'AQAHhQfpU6QfuQFAF4dHAQBFAwABAQCScjdU0gEBAJJyN1TS',
            'dtm_token': 'AQAHhQfpU6QfuQFAF4dHAQBFAwABAQCScjdU0gEBAJJyN1TS',
            '_cq_duid': '1.1732804391.bnn9DxlWGRLirpZ9',
            '_fbp': 'fb.2.1732804391754.760028116510946819',
            '_tt_enable_cookie': '1',
            '_ttp': 'OH7N5ltWww7b4_TvrqXpCTm3ux0.tt.2',
            '_rlid': 'aff60d02-7ae9-4446-bcc5-b05e71496439',
            'analytic_id': '1732804396241883',
            'AwinChannelCookie': 'organic',
            '_clck': '16p20h7%7C2%7Cfrf%7C0%7C1793',
            '__privaci_cookie_consent_uuid': 'afbc327b-86be-4c06-92b4-85e78e163434:10,afbc327b-86be-4c06-92b4-85e78e163434:11',
            '__privaci_cookie_consent_generated': 'afbc327b-86be-4c06-92b4-85e78e163434:11',
            '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3Anull%2C%22expiryDate%22%3A%222025-12-04T02%3A37%3A43.638Z%22%7D',
            'device-id': '0bc78ae8-ec76-46ed-b48c-e460e7f0d98a',
            'session-id': '9fad76b6-ebcc-45d7-9deb-75e1b0d34c14',
            '__cf_bm': 'ZdLbgzMs74rA48FV31aO4WgkbZpRUOeTPxBOGOlblH0-1733347578-1.0.1.1-6Mz4qiJewzFGMdBJT8oaKOmQktrvZ7Q1wQ7pyGSLhaZ8ZEm4NpV8wZQhJNXKjnm14L_U21CuvP4FVh2apjWyCQ',
            '_cfuvid': 'M_JIwCdF.9WjiqkTYZQ0OwDKBaZACYQNIiL8OgKkM_k-1733347578980-0.0.1.1-604800000',
            '_gcl_gs': '2.1.k1$i1733347186$u142539168',
            '__utmzz': 'utmcsr=google_branding|utmcmd=sem|utmccn=branding',
            '__utmzzses': '1',
            '_ga_XSP6W5L7L1': 'GS1.1.1733347188.6.0.1733347188.60.0.0',
            '_gcl_aw': 'GCL.1733347189.CjwKCAiAmMC6BhA6EiwAdN5iLR4lx4xqUc7OIm2IkfN6e_ZuzHGG1Z0sTQHsggJcd59HpGuzHhA9QRoCVWwQAvD_BwE',
            '_gcl_dc': 'GCL.1733347189.CjwKCAiAmMC6BhA6EiwAdN5iLR4lx4xqUc7OIm2IkfN6e_ZuzHGG1Z0sTQHsggJcd59HpGuzHhA9QRoCVWwQAvD_BwE',
            '_cq_suid': '1.1733347190.ZD28uUwY9L9eXHtL',
            '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22YRiPuGCC2f0gqB4NIfNX%22%2C%22expiryDate%22%3A%222025-12-04T21%3A19%3A50.769Z%22%7D',
            '_clsk': '1tcm4mc%7C1733347191641%7C1%7C0%7Ce.clarity.ms%2Fcollect',
            '__privaci_cookie_no_action': '{"status":"no-action-consent"}',
            '_ga_SHP4RTV3MH': 'GS1.1.1733347188.6.0.1733347207.41.0.0',
        }
        
    def get_title(self):
        return self.soup.find('h2', class_='text-text').text

    def get_price(self):
        script_text = self.soup.find_all('script')
        regex = re.compile(r'"Value":\d+\.\d+')

        for line in script_text:
            match = re.search(regex, line.text)
            if match:
                return float(match.group().split(":")[1])

        return 0.0
