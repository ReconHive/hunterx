from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field


@dataclass(slots=True)
class TakeoverFingerprint:

    service: str

    cname_patterns: list[str]

    #
    # confidence:
    #   high   -> cname pattern + fingerprint sourced directly
    #             from can-i-take-over-xyz's documented data
    #   medium -> sourced fingerprint, but generic-ish text or
    #             an approximated/simplified signature
    #   low    -> cname pattern inferred from general knowledge,
    #             not documented in the source db - verify
    #             manually before trusting
    #
    confidence: str = "high"

    signature: str | None = None

    expected_status: int | None = None

    #
    # If True, this service is only exploitable when the CNAME
    # target itself fails to resolve (NXDOMAIN). A body/signature
    # check is not applicable - there's no live host to fetch.
    #
    nxdomain_only: bool = False


#
# Source: EdOverflow/can-i-take-over-xyz (fingerprints.json).
# Only entries marked "Vulnerable" or "Edge case" are included;
# "Not vulnerable" entries (CloudFront, Firebase, Zendesk, HubSpot,
# Fastly, Google Cloud Storage, Google Sites, Squarespace, WP Engine,
# Statuspage, UserVoice, Akamai, GitLab, Desk, Dreamhost, Feedpress,
# Instapage, Key CDN, Kinsta, Mailchimp, Sendgrid, Unbounce, Mashery)
# are deliberately excluded to avoid false positives.
#

FINGERPRINTS: list[TakeoverFingerprint] = [

    #
    # --- High confidence: cname + fingerprint both sourced ---
    #

    TakeoverFingerprint(
        service="AWS Elastic Beanstalk",
        cname_patterns=["elasticbeanstalk.com"],
        nxdomain_only=True,
    ),

    TakeoverFingerprint(
        service="AWS S3",
        cname_patterns=["s3.amazonaws.com"],
        signature="The specified bucket does not exist",
    ),

    TakeoverFingerprint(
        service="Agile CRM",
        cname_patterns=["agilecrm.com"],
        signature="Sorry, this page is no longer available",
    ),

    TakeoverFingerprint(
        service="Airee.ru",
        cname_patterns=["airee.ru"],
        signature="Ошибка 402",
    ),

    TakeoverFingerprint(
        service="Anima",
        cname_patterns=["animaapp.io"],
        signature="The page you were looking for does not exist",
    ),

    TakeoverFingerprint(
        service="Bitbucket",
        cname_patterns=["bitbucket.io"],
        signature="Repository not found",
    ),

    TakeoverFingerprint(
        service="Discourse",
        cname_patterns=["trydiscourse.com"],
        nxdomain_only=True,
    ),

    TakeoverFingerprint(
        service="Gemfury",
        cname_patterns=["furyns.com"],
        signature="404: This page could not be found",
        confidence="medium",
    ),

    TakeoverFingerprint(
        service="Ghost",
        cname_patterns=["ghost.io"],
        signature="Site unavailable",
    ),

    TakeoverFingerprint(
        service="HatenaBlog",
        cname_patterns=["hatenablog.com"],
        signature="404 Blog is not found",
    ),

    TakeoverFingerprint(
        service="Help Juice",
        cname_patterns=["helpjuice.com"],
        signature="We could not find what you're looking for",
    ),

    TakeoverFingerprint(
        service="Help Scout",
        cname_patterns=["helpscoutdocs.com"],
        signature="No settings were found for this company",
    ),

    TakeoverFingerprint(
        service="Helprace",
        cname_patterns=["helprace.com"],
        expected_status=301,
        confidence="medium",
    ),

    TakeoverFingerprint(
        service="JetBrains YouTrack",
        cname_patterns=["youtrack.cloud"],
        signature="is not a registered InCloud YouTrack",
    ),

    TakeoverFingerprint(
        service="LaunchRock",
        cname_patterns=["launchrock.com"],
        expected_status=500,
        confidence="medium",
    ),

    TakeoverFingerprint(
        service="Microsoft Azure",
        cname_patterns=[
            "cloudapp.net",
            "cloudapp.azure.com",
            "azurewebsites.net",
            "blob.core.windows.net",
            "azure-api.net",
            "azurehdinsight.net",
            "azureedge.net",
            "azurecontainer.io",
            "database.windows.net",
            "azuredatalakestore.net",
            "search.windows.net",
            "azurecr.io",
            "redis.cache.windows.net",
            "servicebus.windows.net",
            "visualstudio.com",
        ],
        nxdomain_only=True,
    ),

    TakeoverFingerprint(
        service="Ngrok",
        cname_patterns=["ngrok.io"],
        signature="not found",
        confidence="medium",
    ),

    TakeoverFingerprint(
        service="Readme.io",
        cname_patterns=["readme.io"],
        signature="creators of this project are still working",
    ),

    TakeoverFingerprint(
        service="Strikingly",
        cname_patterns=["s.strikinglydns.com"],
        signature="PAGE NOT FOUND",
    ),

    TakeoverFingerprint(
        service="Surge.sh",
        cname_patterns=["surge.sh"],
        signature="project not found",
    ),

    TakeoverFingerprint(
        service="SurveySparrow",
        cname_patterns=["surveysparrow.com"],
        signature="Account not found",
    ),

    TakeoverFingerprint(
        service="Uberflip",
        cname_patterns=["read.uberflip.com"],
        signature="does not provide a hub",
    ),

    TakeoverFingerprint(
        service="UptimeRobot",
        cname_patterns=["stats.uptimerobot.com"],
        signature="page not found",
        confidence="medium",
    ),

    TakeoverFingerprint(
        service="WordPress",
        cname_patterns=["wordpress.com"],
        signature="Do you want to register",
    ),

    TakeoverFingerprint(
        service="Worksites",
        cname_patterns=["worksites.net"],
        signature="the website you're looking for doesn't exist",
    ),

    #
    # --- Sourced fingerprint, cname pattern inferred (low/medium) ---
    #

    TakeoverFingerprint(
        service="Canny",
        cname_patterns=["canny.io"],
        signature="There is no such company",
        confidence="low",
    ),

    TakeoverFingerprint(
        service="Pantheon",
        cname_patterns=["pantheonsite.io"],
        signature="404 error unknown site",
        confidence="medium",
    ),

    TakeoverFingerprint(
        service="Pingdom",
        cname_patterns=["stats.pingdom.com"],
        signature="couldn't find the status page",
        confidence="medium",
    ),

    TakeoverFingerprint(
        service="Readthedocs",
        cname_patterns=["readthedocs.io"],
        signature="the URL that you entered does not exist",
        confidence="low",
    ),

    TakeoverFingerprint(
        service="Short.io",
        cname_patterns=["short.io"],
        signature="Link does not exist",
        confidence="medium",
    ),

    #
    # --- Edge cases: sourced fingerprint, but platform-side fixes
    # mean these are often (not always) already mitigated. Worth
    # flagging, needs manual confirmation before reporting. ---
    #

    TakeoverFingerprint(
        service="GitHub Pages",
        cname_patterns=["github.io"],
        signature="There isn't a GitHub Pages site here",
        confidence="low",
    ),

    TakeoverFingerprint(
        service="Heroku",
        cname_patterns=["herokuapp.com"],
        signature="No such app",
        confidence="low",
    ),

    TakeoverFingerprint(
        service="Netlify",
        cname_patterns=["netlify.app"],
        signature="Not Found - Request ID",
        confidence="low",
    ),

    TakeoverFingerprint(
        service="Shopify",
        cname_patterns=["myshopify.com"],
        signature="Sorry, this shop is currently unavailable",
        confidence="low",
    ),

    TakeoverFingerprint(
        service="Tumblr",
        cname_patterns=["domains.tumblr.com"],
        signature="doesn't currently exist at this address",
        confidence="low",
    ),

    TakeoverFingerprint(
        service="Vercel",
        cname_patterns=["vercel-dns.com", "vercel.app"],
        signature="DEPLOYMENT_NOT_FOUND",
        confidence="low",
    ),

    TakeoverFingerprint(
        service="Webflow",
        cname_patterns=["webflow.io"],
        signature="doesn't exist or has been moved",
        confidence="low",
    ),

]


def match(
    cname: str,
) -> TakeoverFingerprint | None:

    cname = cname.lower()

    for fingerprint in FINGERPRINTS:

        for pattern in fingerprint.cname_patterns:

            if pattern in cname:

                return fingerprint

    return None