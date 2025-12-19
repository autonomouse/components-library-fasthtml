"""Health check routes for FastHTML applications.

Provides standard health check endpoints for container orchestration
and monitoring. These are generic routes that can be extended with
app-specific component checks.

Usage:
    from fasthtml.common import fast_app
    from components_library.services import register_health_routes

    app, rt = fast_app()

    # Basic health routes
    register_health_routes(rt, version="1.0.0", app_name="My App")

    # With custom component checks
    def check_database():
        return {"connected": True, "latency_ms": 5}

    register_health_routes(
        rt,
        version="1.0.0",
        app_name="My App",
        component_checks={"database": check_database},
    )
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from starlette.responses import JSONResponse


def register_health_routes(
    rt: Any,
    version: str = "0.0.0",
    app_name: str = "Labs App",
    component_checks: dict[str, Callable[[], dict[str, Any]]] | None = None,
) -> None:
    """Register health check routes.

    Args:
        rt: The FastHTML route decorator
        version: Application version string
        app_name: Application name for status response
        component_checks: Optional dict of component name to check function.
            Each function should return a dict with component status info.
    """

    @rt("/health")
    def health_liveness() -> JSONResponse:
        """Basic liveness check.

        Returns 200 OK if the application is running.
        Used by container orchestrators for liveness probes.
        """
        return JSONResponse(
            {
                "status": "ok",
                "version": version,
            }
        )

    @rt("/health/ready")
    def health_readiness() -> JSONResponse:
        """Readiness check including component status.

        Returns 200 OK if the application is ready to serve requests.
        Includes status of any registered component checks.
        """
        status_data: dict[str, Any] = {
            "status": "ok",
            "version": version,
            "app_name": app_name,
        }

        # Run component checks if provided
        if component_checks:
            components: dict[str, Any] = {}
            warnings: list[str] = []

            for name, check_fn in component_checks.items():
                try:
                    components[name] = check_fn()
                except Exception as e:
                    components[name] = {"error": str(e)}
                    warnings.append(f"{name}: {e}")

            status_data["components"] = components

            if warnings:
                status_data["warnings"] = warnings

        return JSONResponse(status_data)
