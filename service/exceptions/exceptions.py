from typing import Any, Dict, Optional

from fastapi import HTTPException, status


class CredentialsException(HTTPException):
    def __init__(
        self,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
        status_code=status.HTTP_401_UNAUTHORIZED,
    ) -> None:
        super().__init__(status_code, detail, headers)
