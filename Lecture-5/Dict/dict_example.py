import json


json_object = """{
    "signature_request_id": "7fd2659d5b33b85a70311eb84b241093d056b58e",
    "test_mode": true,
    "title": "The NDA we talked about",
    "original_title": "The NDA we talked about",
    "subject": "The NDA we talked about",
    "message": "Please sign this NDA and then we can discuss more.",
    "metadata": {},
    "created_at": 1604032043,
    "is_complete": false,
    "is_declined": false,
    "has_error": false,
    "custom_fields": [],
    "response_data": [],
    "signing_url": null,
    "signing_redirect_url": null,
    "signatures": [
      {
        "signature_id": "55475199982fe6e95415c11e9bf71ed5",
        "has_pin": false,
        "signer_email_address": "pavlo1@example.com",
        "signer_name": "Pavlo_1",
        "signer_role": null,
        "order": null,
        "status_code": "awaiting_signature",
        "signed_at": null,
        "last_viewed_at": null,
        "last_reminded_at": null,
        "error": null
      },
      {
        "signature_id": "3f4a07b19a2ce4da5b747d5458e094fd",
        "has_pin": false,
        "signer_email_address": "pavlo2@example.net",
        "signer_name": "Pavlo_2",
        "signer_role": null,
        "order": null,
        "status_code": "awaiting_signature",
        "signed_at": null,
        "last_viewed_at": null,
        "last_reminded_at": null,
        "error": null
      }
    ],
    "cc_email_addresses": [],
    "template_ids": null,
    "client_id": "ce221ed6e6a930eac0149c64e6b5a6eb"
  }"""
dict_object = json.loads(json_object)
list_keys = ["client_id", "signature_request_id", "signatures"]
signatures_list_keys = ["signature_id", "signer_email_address", "signer_name"]

get_embedded_urls = {key: dict_object[key] for key in list_keys}
signatures = [{key: signature[key] for key in signatures_list_keys} for signature in get_embedded_urls["signatures"]]
get_embedded_urls["signatures"] = signatures
print("get_embedded_urls: ", get_embedded_urls)