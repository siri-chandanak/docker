FROM bitnami/dotnet-sdk

COPY FisrtProj.csproj .

COPY Program.cs .

RUN dotnet restore

RUN dotnet publish -c Release -o out

ENTRYPOINT ["dotnet", "out/FisrtProj.dll"]