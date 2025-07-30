from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qa.baseplatform.online/games")
    # Обработчик для синхронного API
    def handle_route(route, request):
        if "api/target-endpoint" in request.url:
            time.sleep(2)  # задержка 2 секунды
        route.continue_()
    context.route("**/healthcheck", handle_route)


    browser.close()